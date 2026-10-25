export const inviteBase = "https://boksday.github.io/daywrap/s/";

export function inviteState(address) {
  const url = new URL(address);
  const token = /^[0-9a-f]{32}$/.test(url.hash.slice(1)) ? url.hash.slice(1) : null;
  const requestedStatus = url.searchParams.get("status");
  const status = ["expired", "closed", "error"].includes(requestedStatus)
    ? requestedStatus
    : token
      ? "ready"
      : "invalid";
  return {
    status,
    appLink: token ? `daywrap://share#${token}` : null,
    retryLink: token ? `${inviteBase}#${token}` : null,
  };
}
