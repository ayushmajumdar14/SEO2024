const fetch = require('node-fetch');
const {google} = require('googleapis');

// Function to get industry from Diffbot
async function getIndustryFromDiffbot(url) {
    const api_url = "https://api.diffbot.com/v3/article";
    const api_key = "cf4cd0544b4bbae862e8b792c7959881"; // Replace with your Diffbot API key
    const params = new URLSearchParams({ token: api_key, url: url });
    
    try {
        const response = await fetch(`${api_url}?${params}`);
        if (!response.ok) throw new Error(`Error fetching data from Diffbot API: ${response.statusText}`);
        const data = await response.json();
        if ('objects' in data && data.objects.length) {
            return data.objects[0];
        }
    } catch (e) {
        console.error(e.message);
    }
    return null;
}

// Function to extract specific industry
function getSpecificIndustry(data) {
    if (data) {
        const tags_list = data.tags || [];
        const specific_industry = tags_list.map(tag => tag.name || '').filter(name => name).join(', ');
        return specific_industry || null;
    }
    return null;
}

// Function to crawl website and get industries
async function crawlWebsite(start_url) {
    let current_url = start_url;
    let industries = [];

    while (new Set(industries).size < 3) { // Loop until there are at least three distinct industries
        const article_data = await getIndustryFromDiffbot(current_url);

        if (article_data) {
            const general_industries = article_data.categories || [];
            const specific_industry = getSpecificIndustry(article_data);

            if (specific_industry) {
                industries.push(...specific_industry.split(', '));
            } else if (general_industries.length) {
                const general_industries_names = general_industries.map(category => category.name || '');
                industries.push(...general_industries_names);
            }
        }

        // Break the loop if three distinct industries have been identified
        if (new Set(industries).size >= 4) {
            break;
        }
    }

    // Calculate the three most common industries
    const counts = industries.reduce((acc, industry) => {
        acc[industry] = (acc[industry] || 0) + 1;
        return acc;
    }, {});
    return Object.keys(counts).sort((a, b) => counts[b] - counts[a]).slice(0, 4);
}

// Function to perform Google Custom Search
async function googleSearch(search_terms) {
    const api_key = "AIzaSyBHKRK8lSx0-V06ftxcccuF4Qo3jsIySK4"; // Your Google API key
    const cse_id = "522dadda8ecdf466a"; // Your Custom Search Engine ID
    const combined_search_query = search_terms.join(' OR '); // Combine industries into one search query
    const customsearch = google.customsearch('v1');
    
    try {
        const res = await customsearch.cse.list({
            cx: cse_id,
            q: combined_search_query,
            auth: api_key,
            num: 20 // Get 20 results
        });
        const links = res.data.items ? res.data.items.map(item => item.link) : [];
        return links;
    } catch (error) {
        console.error('Error during Google Custom Search:', error);
        return [];
    }
}

// Function to extract keywords from articles
async function extractKeywordsFromLinks(links) {
    let all_keywords = new Set();
    for (const link of links) {
        if (all_keywords.size >= 20) break; // Stop if we have gathered at least 20 unique keywords
        const article_data = await getIndustryFromDiffbot(link);
        if (article_data && article_data.tags) {
            article_data.tags.slice(0, 5).forEach(tag => {
                if (tag.label) all_keywords.add(tag.label);
            });
            if (all_keywords.size >= 20) break; // Break if we have reached 20 unique keywords
        }
    }
    return Array.from(all_keywords); // Return the collected unique keywords, aiming for at least 12
}

// Main function to integrate both scrapers and the new keywords extractor
async function main() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question('Enter the link to start crawling: ', async (userLink) => {
        const industries = await crawlWebsite(userLink);
        if (industries.length) {
            console.log("The three most common industries are:", industries.join(', '));
            console.log("\nLinks that fit well into all three industries:");
            const links = await googleSearch(industries);
            links.forEach(link => console.log(link));
            
            console.log("\nExtracting keywords from the articles...");
            const keywords = await extractKeywordsFromLinks(links);
            if (keywords.length) {
                console.log("Unique keywords extracted from the articles:", keywords.join(', '));
            } else {
                console.log("No keywords could be extracted.");
            }
        } else {
            console.log("Failed to identify three distinct industries.");
        }
        readline.close();
    });
}

if (require.main === module) {
    main();
}