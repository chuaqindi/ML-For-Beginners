import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import * as ort from 'onnxruntime-web';
import {featureVector, recommend} from './recommender.mjs';

const metadata = JSON.parse(await readFile(new URL('./metadata.json', import.meta.url)));
const fixtures = JSON.parse(await readFile(new URL('./fixtures.json', import.meta.url)));
assert.throws(() => featureVector([], metadata.features), /Select/);
assert.throws(() => featureVector(['unknown ingredient'], metadata.features), /Unknown/);
const first = featureVector([metadata.features[0]], metadata.features);
assert.equal(first[0], 1);
assert.equal(first.reduce((a, b) => a + b), 1);
assert.equal(featureVector([metadata.features[1]], metadata.features)[0], 0);
assert.deepEqual(recommend(metadata.features, metadata.classes[0], metadata), []);
ort.env.wasm.numThreads = 1;
const session = await ort.InferenceSession.create(
  new Uint8Array(await readFile(new URL('./model.onnx', import.meta.url))),
  {executionProviders: ['wasm']}
);
for (const fixture of fixtures) {
  const vector = featureVector(fixture.selected, metadata.features);
  const output = await session.run({ingredients: new ort.Tensor('float32', vector, [1, vector.length])});
  assert.equal(output.label.data[0], fixture.label);
  const probabilities = output.probabilities.data;
  probabilities.forEach((p, i) => assert.ok(Math.abs(p - fixture.probabilities[i]) < 0.0001));
  assert.deepEqual(recommend(fixture.selected, fixture.label, metadata), fixture.recommendations);
}
await session.release();
console.log('Passed: validation, fresh vectors, excluded selections, and 3 Python/WASM inference fixtures.');
