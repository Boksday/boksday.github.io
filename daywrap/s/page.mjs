import { inviteState } from "./share.mjs";
import { chooseLocale, translations } from "./translations.mjs";

const locale = chooseLocale(navigator.languages ?? [navigator.language]);
const copy = translations[locale];
document.documentElement.lang = locale;
document.documentElement.dir = locale === "ar" ? "rtl" : "ltr";

for (const id of ["open", "retry", "install", "verification", "resend"]) {
  document.getElementById(id).textContent = copy[id];
}
function render() {
  const state = inviteState(window.location.href);
  document.title = `${copy[state.status]} · Daywrap`;
  document.getElementById("title").textContent = copy[state.status];
  const ready = state.status === "ready";
  document.getElementById("message").textContent = ready ? copy.message : "";
  document.getElementById("message").hidden = !ready;
  document.getElementById("resend").hidden = ready;

  for (const [id, href] of [
    ["open", state.appLink],
    ["retry", state.retryLink],
  ]) {
    const link = document.getElementById(id);
    if (href) link.href = href;
    else link.removeAttribute("href");
    link.hidden = !href;
  }
}

render();
window.addEventListener("hashchange", render);
window.addEventListener("popstate", render);
