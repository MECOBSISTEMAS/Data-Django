function getCookie(cookieName="") {
  const cookie = window.document.cookie
  .split(';')
  .map(cookie => cookie.trim())
  .find(cookie => cookie.startsWith(cookieName + '='))

  if (cookie) {
    //! retornar o valor do cookie sem o nome do cookie
    return cookie.split('=')[1]
  }
  return ""
}

