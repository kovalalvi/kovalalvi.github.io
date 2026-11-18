// Heading rail for posts: a column of dashes left of the text, one per h2/h3 (h2 only if front matter has toc: h2).
// Hover shows the titles, the current section is highlighted. Hidden on narrow screens by CSS.
(() => {
  const onlyH2 = document.querySelector("article[data-toc=h2]");
  const headings = [...document.querySelectorAll(onlyH2 ? "article h2[id]" : "article h2[id], article h3[id]")];
  if (headings.length < 3) return;

  const rail = document.createElement("nav");
  rail.className = "toc";
  rail.setAttribute("aria-label", "Contents");
  const links = headings.map((h) => {
    const a = document.createElement("a");
    a.href = "#" + h.id;
    a.className = h.tagName === "H3" ? "sub" : "";
    a.innerHTML = `<i></i><span>${h.textContent}</span>`;
    rail.append(a);
    return a;
  });
  document.body.append(rail);

  let ticking = false;
  const update = () => {
    ticking = false;
    const line = window.innerHeight * 0.3;
    let current = -1;
    headings.forEach((h, i) => { if (h.getBoundingClientRect().top < line) current = i; });
    links.forEach((a, i) => a.classList.toggle("active", i === current));
  };
  window.addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
})();
