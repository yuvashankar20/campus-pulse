const API = "http://127.0.0.1:5000";

let charts = [];

function clearCharts() {
    charts.forEach(c => c.destroy());
    charts = [];
}

async function loadDashboard() {

    const data = await fetch(`${API}/data`).then(res => res.json());
    const metrics = await fetch(`${API}/metrics`).then(res => res.json());

    document.getElementById("overallAvg").innerText = metrics.overall_average;
    document.getElementById("bestFacility").innerText = metrics.best_facility;
    document.getElementById("worstFacility").innerText = metrics.worst_facility;
    document.getElementById("totalCount").innerText = data.length;

    clearCharts();

    // ---------- OVERALL BAR ----------
    const overall = metrics.average_by_facility;
    charts.push(new Chart(document.getElementById("overallBar"), {
        type: "bar",
        data: {
            labels: Object.keys(overall),
            datasets: [{
                label: "Avg Score",
                data: Object.values(overall)
            }]
        },
        options: { scales: { y: { min: 0, max: 5 } } }
    }));

    // ---------- FACILITY DONUTS ----------
    function facilityChart(name, canvasId) {
        const dist = [0,0,0,0,0];
        data.filter(d => d.facility_rated === name)
            .forEach(d => dist[d.satisfaction_score - 1]++);

        charts.push(new Chart(document.getElementById(canvasId), {
            type: "doughnut",
            data: {
                labels: ["1","2","3","4","5"],
                datasets: [{ data: dist }]
            }
        }));
    }

    facilityChart("Library", "libraryChart");
    facilityChart("Hostel", "hostelChart");
    facilityChart("Sports Center", "sportsChart");

    // ---------- YEAR LINE ----------
    const yearMap = {};
    data.forEach(d => {
        yearMap[d.academic_year] ??= [];
        yearMap[d.academic_year].push(d.satisfaction_score);
    });

    const years = Object.keys(yearMap);
    const avg = years.map(y =>
        yearMap[y].reduce((a,b)=>a+b,0)/yearMap[y].length
    );

    charts.push(new Chart(document.getElementById("yearChart"), {
        type: "line",
        data: {
            labels: years,
            datasets: [{
                label: "Avg Satisfaction",
                data: avg,
                tension: 0.3
            }]
        }
    }));
}

loadDashboard();
