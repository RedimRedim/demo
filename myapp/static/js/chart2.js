const data = {
  labels: [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
  ],
  datasets: [
    {
      label: "Weekly Sales",
      data: [18, 12, 6, 9, 12, 3, 9, 18, 12, 6, 9, 12, 3, 9],
      backgroundColor: ["rgba(255, 26, 104, 0.2)"],
      borderColor: ["rgba(255, 26, 104, 1)"],
      borderWidth: 1,
    },
  ],
};

// config
const config = {
  type: "line",
  data,
  options: {
    maintainAspectRatio: false,
    pointRadius: 5,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

// render init block
const myChart = new Chart(document.getElementById("myChart"), config);

// scroll bar adjustment
const containerBody = document.querySelector(".containerBody");
const totalLabels = myChart.data.labels.length;
if (totalLabels > 7) {
  const newWidth = 700 + (totalLabels - 7) * 50; // Adjust the multiplier for better spacing
  containerBody.style.width = `${newWidth}px`;
}
