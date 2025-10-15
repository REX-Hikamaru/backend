document.addEventListener("DOMContentLoaded", () => {
  const dataTag = document.getElementById("topics-data");
  const topics = JSON.parse(dataTag.textContent);
  renderExamples(topics);
});

function renderExamples(topics) {
  const container = document.getElementById("topics-container");
  Object.keys(topics).forEach(key => {
    const section = document.createElement("section");
    section.innerHTML = `
      <h2>${key}</h2>
      <p>${topics[key].説明}</p>
      <pre><code>${topics[key].例}</code></pre>
    `;
    container.appendChild(section);
  });
}
