// articles/static/articles/js/fold-post.js

// Находим все кнопки сворачивания
var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var post = e.target.closest(".one-post"); // родитель статьи

        // Переключаем класс folded у поста
        post.classList.toggle("folded");

        // Меняем текст кнопки
        if (post.classList.contains("folded")) {
            e.target.innerHTML = "Развернуть";
        } else {
            e.target.innerHTML = "Свернуть";
        }
    });
}
