const reversedOrderDate = [...orderDate].reverse();
const reversedRatio = [...ratio].reverse();
const reversedcompletedOrders = [...completedOrders].reverse();

createChart(
  (labels = reversedOrderDate),
  (dataset = reversedRatio),
  (title = "Test Company 2024 - Sales Ratio"),
  (chartId = "myChart1"),
  (containerBodyId = "#containerBody1")
);

createChart(
  (labels = reversedOrderDate),
  (dataset = reversedcompletedOrders),
  (title = "Test Company 2024 -  Completed Orders"),
  (chartId = "myChart2"),
  (containerBodyId = "#containerBody2")
);

function createChart(labels, dataset, title, containerBodyClass) {
  const data = {
    labels: labels,
    datasets: [
      {
        label: title,
        data: dataset,
        backgroundColor: "rgba(255, 26, 104, 0.2)", // Color of the filled area
        borderColor: "rgba(255, 26, 104, 1)", // Color of the line
        borderWidth: 1,
        pointRadius: 7,
        pointHoverRadius: 10,
        hoverBackgroundColor: "rgba(54, 162, 235, 0.2)", // Color when hovered
        hoverBorderColor: "rgba(54, 162, 235, 1)", // Border color when hovered
        hoverBorderWidth: 2, // Border width when hovered
        fill: true, // Fill the area under the line
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
          beginAtZero: false,
        },
      },
      plugins: {
        legend: { position: "top", align: "start" },
        title: {
          display: true,
          text: title,
          font: {
            size: 16,
          },
          align: "start",
        },
      },
    },
  };

  // render init block
  const myChart = new Chart(document.getElementById(chartId), config);

  // scroll bar adjustment
  const containerBody = document.querySelector(containerBodyId);
  const totalLabels = myChart.data.labels.length;
  if (totalLabels > 7) {
    const newWidth = 700 + (totalLabels - 7) * 50; // Adjust the multiplier for better spacing
    containerBody.style.width = `${newWidth}px`;
  }
}
