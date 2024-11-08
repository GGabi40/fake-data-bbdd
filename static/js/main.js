document.getElementById("generate-sql-btn").addEventListener("click", function () {
    const table = document.querySelector("table");

    let selectedData = [];
    // Recorremos los checkboxes seleccionados
    document.querySelectorAll("input[name='datos']:checked").forEach(
        function (checkbox) {
        selectedData.push(checkbox.value); // Guardamos el valor de los checkboxes
      }
    );

    let sqlOutput = "INSERT INTO nombre_tabla (" + selectedData.join(", ") + ") VALUES\n";

    const rows = table.querySelectorAll("tbody tr");
    rows.forEach((row, index) => {
      const cells = row.querySelectorAll("td");
      const values = Array.from(cells).map((cell) => `'${cell.innerText}'`);
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


let texto = document.getElementById("sql-output").value;
const copiar = async () => {
    try {
        await navigator.clipboard.writeText(texto);
    } catch (error) {
        console.error('Un error! ', error);
    }
}