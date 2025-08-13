/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
document.addEventListener("DOMContentLoaded", () => {
  const productosData = JSON.parse(
    document.getElementById("productos-data").textContent
  );

  const nombres = productosData.map((producto) => producto.nombre);
  const votos = productosData.map((producto) => producto.votos);

  console.log("Nombres:", nombres);
  console.log("Votos:", votos);

  const barConfig = {
    type: "bar",
    data: {
      labels: nombres,
      datasets: [
        {
          label: "votos",
          backgroundColor: "#0694a2",
          // borderColor: window.chartColors.red,
          borderWidth: 1,
          data: votos,
        },
      ],
    },
    options: {
      responsive: true,
      legend: {
        display: false,
      },
    },
  };

  const barsCtx = document.getElementById("bars");
  window.myBar = new Chart(barsCtx, barConfig);
});
