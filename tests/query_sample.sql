-- Find unfinished tasks and sort them by priority.
SELECT
    task_id,
    title,
    priority,
    created_at
FROM tasks
WHERE completed = FALSE
  AND priority >= 2
ORDER BY priority DESC, created_at ASC;