var board = document.getElementById("board");
for (let field = 1; field <= 9; field++) {
  board.appendChild(createField("-", field));
}

function createField(value, id) {
  let field = document.createElement("div");
  let front = document.createElement("div");
  let left = document.createElement("div");
  field.className = "field";
  front.className = "front";
  left.className = "left";
  field.appendChild(left);
  field.appendChild(front);
  console.log(field);
  field.id = id;
  //field.innerText = value;
  return field;
}
