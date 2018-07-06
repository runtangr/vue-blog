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
	return request(`${base}/tags`)
}

export {
	requestArticleList,
	requestArticle,
	requestTags,
}

