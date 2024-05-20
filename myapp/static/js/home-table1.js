// Pagination variables
let currentPage = 1;
const rowsPerPage = 10;

// Function to render the table body
function renderTableBody(orderDate, ratio, completedOrders, page) {
  const table1Body = document.getElementById("table1-body");
  table1Body.innerHTML = "";

  const start = (page - 1) * rowsPerPage;
  const end = start + rowsPerPage;
  const paginatedData = orderDate.slice(start, end);

  for (let i = 0; i < paginatedData.length; i++) {
    const row = document.createElement("tr");

    const cell2 = document.createElement("td");
    cell2.textContent = orderDate[start + i];
    row.appendChild(cell2);

    const cell3 = document.createElement("td");
    cell3.textContent = ratio[start + i];
    row.appendChild(cell3);

    const cell4 = document.createElement("td");
    cell4.textContent = completedOrders[start + i];
    row.appendChild(cell4);

    table1Body.appendChild(row);
  }
}

// Function to setup pagination controls
function setupPagination(orderDate, ratio, completedOrders, rowsPerPage) {
  const pagination = document.getElementById("pagination");
  pagination.innerHTML = "";

  const pageCount = Math.ceil(orderDate.length / rowsPerPage);

  for (let i = 1; i <= pageCount; i++) {
    const li = document.createElement("li");
    li.classList.add("page-item");
    if (i === currentPage) {
      li.classList.add("active");
    }

    const a = document.createElement("a");
    a.classList.add("page-link");
    a.href = "#";
    a.textContent = i;

    a.addEventListener("click", function (e) {
      e.preventDefault();
      currentPage = i;
      renderTableBody(orderDate, ratio, completedOrders, currentPage);
      setupPagination(orderDate, ratio, completedOrders, rowsPerPage);
    });

    li.appendChild(a);
    pagination.appendChild(li);
  }
}

// Initial render
renderTableBody(orderDate, ratio, completedOrders, currentPage);
setupPagination(orderDate, ratio, completedOrders, rowsPerPage);
