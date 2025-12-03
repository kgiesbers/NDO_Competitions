const input = document.getElementById('competitor-name');
const button = document.getElementById('search-btn');
const container = document.getElementById('competitions-container');

async function fetchCompetitions(name) {
    // Check if a name was entered
    if (!name) return;

    // Build the URL
    const url = `http://127.0.0.1:8000/competition_by_competitor/${encodeURIComponent(name)}`;


    try {
        const response = await fetch(url); // send request to backend
        if (!response.ok) {
            console.error('Error fetching competitions:', response.status);
            container.innerHTML = '<p>Error: Could not fetch competitions</p>';
            return;
        }

        const data = await response.json(); // parse JSON response
        return data; // return the array of competitions
    } catch (err) {
        console.error('Network error:', err);
        container.innerHTML = '<p>Network error occurred</p>';
    }
}

function renderCompetitions(data) {
    container.innerHTML = '';

    if (!data || data.length === 0) {
        container.innerHTML = '<p>No competitions found</p>';
        return;
    }

    data.forEach(item => {
        const div = document.createElement('div');
        div.className = 'competition';
        div.innerHTML = `
            <h2>${item.competition.name}</h2>
            <p>Bracket: ${item.bracket.name}</p>
            <p>Listing: ${item.listing.place}</p>
            <a href="${item.bracket.url}" target="_blank">View competition</a>
        `;
        container.appendChild(div);
    });
}

button.addEventListener('click', async () => {
    const name = input.value.trim(); // get input value
    const competitions = await fetchCompetitions(name); // call API
    renderCompetitions(competitions); // update page
});