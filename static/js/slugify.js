let titleInput = document.querySelector('input[name=title]');
let slugInput = document.querySelector('input[name=slug]');

let slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-') //replace & with '-and-'
        .replace(/[\s\W-]+/g, '-') //  replace spaces, non-word chars and dashes with a single dash
};

titleInput.addEventListener('keyup', (e) => {
    slugInput.setAttribute('value', slugify(titleInput.value));
});