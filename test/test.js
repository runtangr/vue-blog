/**
 * Created by tangr on 2018/5/17.
 */
import axios from 'axios'
const request = (url, options={}, method='get') => {
  let key = ~['delete', 'get', 'head'].indexOf(method) ? 'params' : 'data';
  return axios(Object.assign({'url': url, 'method':method, 'validateStatus': false}, {[key]: options})).then(
    res => res)
}

const requestLogin = () => {
  return request('www.baidu.com', {}, 'get');
}
requestLogin()
