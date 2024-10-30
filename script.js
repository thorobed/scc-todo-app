let todoList = [
    "Demo Task 1",
    "Demo Task 2"
]

const listElement = document.getElementById("list")
const addButton = document.getElementById("add")
const deleteButton = document.getElementById("delete")

function updateTasks() {
    listElement.innerHTML = "";
    for (let i = 0; i < todoList.length; i++) {
        let newTaskElement = document.createElement("li")
        newTaskElement.textContent = todoList[i];
        listElement.appendChild(newTaskElement)
    }
}

function addTask(taskName) {
    todoList.push(taskName)
    updateTasks();
}

function deleteTask() {
    todoList.pop()
        updateTasks()
}

addButton.addEventListener("click", () => {
    const task = prompt("Enter task name")
    addTask(task)
})

deleteButton.addEventListener("click", () => {
    deleteTask()
})

updateTasks();
console.log(listElement);

