function getCookie(cookieName="") {
  const cookie = window.document.cookie
  .split(';')
  .map(cookie => cookie.trim())
  .find(cookie => cookie.startsWith(cookieName + '='))

  if (cookie) {
    return cookie.split('=')[1]
  }
  return ""
}