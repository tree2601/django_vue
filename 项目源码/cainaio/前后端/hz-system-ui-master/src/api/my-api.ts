// @ts-ignore
import result from '/@utils/Axios.ts'

export function registerAccount() {
  return result({
    url:'/api/cainiao/findAllWorld/',
    method:'get',
  })
}

export function gitintiitle(query:any) {
    return result({
        url:'/api/cainiao/gitintiitle/',
        method:'get',
        params:query
    })

}

export function gitinintiitle(query:any) {
    return result({
        url:'/api/cainiao/gitinintiitle/',
        method:'get',
        params:query
    })
}

export function gitcontent(query:any) {
    return result({
        url:'/api/cainiao/gitcontent/',
        method:'get',
        params:query
    })
}


export function getuserinfo() {
    return result({
        url:'/api/hzadmin/userinfo/',
        method:'get',

    })
}




export function putlike(query:any) {
    return result({
        url:'/api/cainiao/putlike/',
        method:'get',
        params:query,
    })
}


export function getlikebyid(query:any) {
    return result({
        url:'/api/cainiao/getlikebyid/',
        method:'get',
        params:query,
    })
}


export function getNameByname(query:any) {
    return result({
        url:'/api/cainiao/getNameByname/',
        method:'get',
        params:query,
    })
}

export function getcainiao(query:any) {
    return result({
        url:'/api/cainiao/getcainiao/',
        method:'get',
        params:query,
    })
}


export function getTuijianForUser(query:any) {
    return result({
        url:'/api/cainiao/getTuijianForUser/',
        method:'get',
        params:query,
    })
}


export function getname(query:any) {
    return result({
        url:'/api/cainiao/getname/',
        method:'get',
        params:query,
    })
}

export function TitleCountAll() {
    return result({
        url:'/api/cainiao/TitleCountAll/',
        method:'get',

    })
}

export function getAllWord() {
    return result({
        url:'/api/cainiao/getAllWord/',
        method:'get',

    })


}

export function getAllWordByc() {
    return result({
        url:'/api/cainiao/getAllWordByc/',
        method:'get',

    })
}