// @ts-ignore
import result from '/@utils/Axios.ts'

export function registerAccount(query:any) {
  return result({
    url:'/api/hzadmin/register/',
    method:'post',
    data:query,
  })
}

export function loginIn(query:any) {
  return result({
    url:'/api/hzadmin/login/',
    method:'post',
    data:query,
  })
}

export function getUserInfo(query:any) {
    return result({
        url:'/api/hzadmin/userinfo/',
        method:'get',
        params:query
    })
}

export function setUserInfo(query:any) {
    return result({
        url:'/api/hzadmin/userinfo/',
        method:'post',
        data:query,
    })
}

export function logout(query:any) {
  return result({
    url:'/api/hzadmin/logout',
    method:'get',
    params:query
  })
}
