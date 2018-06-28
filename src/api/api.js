import axios from 'axios'

const base = `/api`

const request = (url, options={}, method='get') => {
    let key = ~['delete', 'get', 'head'].indexOf(method) ? 'params' : 'data';
    return axios(Object.assign({'url': url, 'method':method, 'validateStatus': false}, {[key]: options})).then(
        res => res)
}

const requestArticleList = params => {
    return request(`${base}/articles`, params)
}

const requestArticle = id => {
    return request(`${base}/article/${id}`)
}

const requestTags = () => {
	return request(`${base}/article/tags`)
}
// requestTagDetial


// export {
// 	requestArticle,
// }

export {
	requestArticleList,
	requestArticle,
	requestTags,
}


// export function requestArticleList(params) {
//   return request({
//     url: base + '/schedule/list',
//     method: 'get',
//     params
//   })
// }

// export function requestList(params) {
//   return request({
//     url: base + '/schedule/list',
//     method: 'get',
//     params
//   })
// }