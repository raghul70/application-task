const API_URL = "http://localhost:8000/tasks";

// Load tasks when page opens
window.onload = function () {
  loadTasks();
};

// GET all tasks
function loadTasks() {
  fetch(API_URL)
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("taskList");
      list.innerHTML = "";

      data.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task.title;
        list.appendChild(li);
      });
    })
    .catch(err => console.log("Error loading tasks:", err));
}

// POST new task
function addTask() {
  const input = document.getElementById("taskInput");
  const title = input.value.trim();

  if (title === "") {
    alert("Task cannot be empty");
    return;
  }

  fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title })
  })
    .then(res => res.json())
    .then(() => {
      input.value = "";
      loadTasks();
    })
    .catch(err => console.log("Error adding task:", err));
}