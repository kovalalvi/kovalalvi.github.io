// Blog index filter: a chip shows only posts of its type; years with nothing left are hidden.
(() => {
  const chips = [...document.querySelectorAll(".filters .chip")];
  const show = (type) => {
    chips.forEach((c) => c.classList.toggle("active", c.dataset.type === type));
    document.querySelectorAll("section.year").forEach((sec) => {
      let any = false;
      sec.querySelectorAll("li").forEach((li) => {
        const on = type === "all" || li.dataset.type === type;
        li.hidden = !on;
        any ||= on;
      });
      sec.hidden = !any;
    });
  };
  chips.forEach((c) => c.addEventListener("click", () => show(c.dataset.type)));
})();
