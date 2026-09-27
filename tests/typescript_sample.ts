type Status = "pending" | "complete";

interface Task {
  id: number;
  title: string;
  status: Status;
}

function findTask<T extends Task>(tasks: T[], id: number): T | undefined {
  return tasks.find((task) => task.id === id);
}

const tasks: Task[] = [
  { id: 1, title: "Review theme", status: "complete" },
  { id: 2, title: "Check syntax colors", status: "pending" },
];

const selected = findTask(tasks, 2);
console.log(selected?.title ?? "Task not found");