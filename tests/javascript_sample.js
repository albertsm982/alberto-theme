const tasks = [
  { title: "Review theme", completed: true },
  { title: "Check syntax colors", completed: false },
];

function summarize(items) {
  const completed = items.filter((item) => item.completed).length;
  return `${completed}/${items.length} tasks completed`;
}

class ThemePreview {
  constructor(name) {
    this.name = name;
  }

  render() {
    console.log(`${this.name}: ${summarize(tasks)}`);
  }
}

new ThemePreview("Alberto Santos").render();