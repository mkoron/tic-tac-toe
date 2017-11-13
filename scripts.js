var board = document.getElementById('board');
for (let field = 1; field <= 9; field++) {
    board.appendChild(createField('-', field));
}

function createField(value, id) {
    let field =  document.createElement('div');
    field.className = 'field';
    field.id = id;
    field.innerText = value;
    return field;
}