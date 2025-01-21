document
  .getElementById("generate-sql-btn")
  .addEventListener("click", function () {
    const table = document.querySelector("table");

    let selectedData = [];

    // Recorremos los checkboxes seleccionados
    document
      .querySelectorAll("input[name='datos']:checked")
      .forEach((checkbox) => {
        selectedData.push(checkbox.value); // Se guarda el valor de los checkboxes
      });

    let sqlOutput =
      "INSERT INTO nombre_tabla (" + selectedData.join(", ") + ") VALUES\n";

    const rows = table.querySelectorAll("tbody tr");
    rows.forEach((row, index) => {
      const cells = row.querySelectorAll("td");
      const values = Array.from(cells).map((cell) => {
        const cellValue = cell.innerText.trim();

        // si es un numero o True o False, no tendrá comillas simples
        if (cellValue === 'True' || cellValue === 'False' || !isNaN(cellValue)) {
          return cellValue
        } else {
          return `'${cellValue}'`
        }

      });

    /* TODO:
      [] True y False sin comillas
      [] Numero de cel sin espacios
    */
      sqlOutput += `(${values.join(", ")})`;

      // Agrega punto y coma al último dato
      if (index < rows.length - 1) {
        sqlOutput += ",\n";
      } else {
        sqlOutput += ";";
      }
    });

    document.getElementById("sql-output").value = sqlOutput;
  });
