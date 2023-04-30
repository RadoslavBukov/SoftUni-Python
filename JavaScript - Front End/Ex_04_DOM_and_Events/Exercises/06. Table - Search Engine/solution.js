function solve() {
  document.querySelector("#searchBtn").addEventListener("click", onClick);
  const searchInput = document.getElementById("searchField");

  function onClick() {
    const searchedWord = searchInput.value;
    const tableRows = Array.from(document.querySelectorAll("tbody tr"));

    for (const row of tableRows) {
      let trimmedTextContent = row.textContent.trim();

      if (row.classList.contains("select")) {
        row.classList.remove("select");
      }
      // Case sensitive (Lower and upper letters)
      if (trimmedTextContent.includes(searchedWord)) {
        row.classList.add("select");
      }
      // // Without case sensitive (Lower and upper letters)
      // if (trimmedTextContent.toLowerCase().includes(searchedWord.toLowerCase())) {
      //   row.classList.add("select");
      // }
    }
    searchInput.value = "";
  }
}
 