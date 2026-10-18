import {featureVector, recommend} from './recommender.mjs';

const status = document.querySelector('#status');
const button = document.querySelector('#predict');
const container = document.querySelector('#ingredients');
const result = document.querySelector('#result');
const selected = new Set();
let revision = 0;
const readable = name => name.replaceAll('_', ' ');

try {
  const response = await fetch('./metadata.json');
  if (!response.ok) throw new Error('Model metadata could not be loaded.');
  const metadata = await response.json();
  ort.env.wasm.numThreads = 1;
  ort.env.wasm.wasmPaths = new URL('./node_modules/onnxruntime-web/dist/', import.meta.url).href;
  const session = await ort.InferenceSession.create('./model.onnx', {executionProviders: ['wasm']});
  for (const name of metadata.features) {
    const label = document.createElement('label');
    const input = document.createElement('input');
    input.type = 'checkbox';
    input.value = name;
    label.append(input, document.createTextNode(` ${readable(name)}`));
    input.addEventListener('change', () => {
      revision++;
      if (input.checked) selected.add(name); else selected.delete(name);
      document.querySelector('#count').textContent = `${selected.size} selected`;
      result.hidden = true;
      status.textContent = 'Ready to suggest additions.';
    });
    container.append(label);
  }
  document.querySelector('#search').addEventListener('input', event => {
    const query = event.target.value.trim().toLowerCase();
    for (const label of container.children) label.hidden = !label.textContent.toLowerCase().includes(query);
  });
  document.querySelector('#clear').addEventListener('click', () => {
    revision++;
    selected.clear();
    for (const input of container.querySelectorAll('input')) input.checked = false;
    result.hidden = true;
    document.querySelector('#count').textContent = '0 selected';
    status.textContent = 'Selection cleared.';
  });
  document.querySelector('#metrics').textContent = `Held-out accuracy ${(metadata.accuracy * 100).toFixed(1)}%; macro F1 ${metadata.macro_f1.toFixed(3)}.`;
  button.disabled = false;
  status.textContent = 'Ready. Select at least one ingredient.';
  button.addEventListener('click', async () => {
    result.hidden = true;
    button.disabled = true;
    try {
      const snapshot = [...selected];
      const requestRevision = revision;
      const vector = featureVector(snapshot, metadata.features);
      status.textContent = 'Finding a match…';
      const output = await session.run({ingredients: new ort.Tensor('float32', vector, [1, vector.length])});
      if (requestRevision !== revision) return;
      const cuisine = output.label.data[0];
      const suggestions = recommend(snapshot, cuisine, metadata);
      document.querySelector('#cuisine').textContent = `${cuisine} cuisine match`;
      const list = document.querySelector('#suggestions');
      list.replaceChildren(...suggestions.map(name => {
        const item = document.createElement('li'); item.textContent = readable(name); return item;
      }));
      result.hidden = false;
      status.textContent = suggestions.length ? 'Three additions to explore.' : 'All ingredients are already selected.';
    } catch (error) {
      status.textContent = error.message;
    } finally {
      button.disabled = false;
    }
  });
} catch (error) {
  status.textContent = `Could not load the model: ${error.message}. Serve this folder over HTTP after running npm install.`;
}
