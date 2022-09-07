window.addEventListener("load", async (event) => {
  await tf
    .loadGraphModel(
      "https://download936.mediafire.com/hpl2wsq1mxrg/56q3xxl3tzo96jp/model.json"
    )
    .catch((error) => {
      console.error(error);
    });
});
