export function featureVector(selected, features) {
  if (!selected.length) throw new Error('Select at least one ingredient.');
  if (selected.some(name => !features.includes(name))) throw new Error('Unknown ingredient.');
  const present = new Set(selected);
  return Float32Array.from(features, name => Number(present.has(name)));
}

export function recommend(selected, cuisine, metadata) {
  const classIndex = metadata.classes.indexOf(cuisine);
  if (classIndex < 0) throw new Error('Unknown cuisine.');
  const present = new Set(selected);
  return metadata.features
    .map((name, index) => ({name, frequency: metadata.prevalence[classIndex][index]}))
    .filter(item => !present.has(item.name))
    .sort((a, b) => b.frequency - a.frequency || (a.name < b.name ? -1 : a.name > b.name ? 1 : 0))
    .slice(0, 3).map(item => item.name);
}
