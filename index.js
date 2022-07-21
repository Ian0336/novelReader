const add = document.querySelector("#add_size");
const sub = document.querySelector("#sub_size");
const body = document.querySelector("#body");
num = 30;
add.addEventListener("click", () => {
  num += 5;
  console.log(num);
  body.style.fontSize = num + "px";
});

sub.addEventListener("click", () => {
  num -= 5;
  body.style.fontSize = num + "px";
});
