import axios from 'axios'

export const user_list = function(){
    return axios.get('http://47.108.235.245:8080/api/user')
    .then(res =>{
        return res
    }).catch(res =>{
        console.log(res)
        return res
    })
}

export const ammeter_info = function(){
    return axios.get('http://47.108.235.245:8080/api/ammeter_info')
    .then(res => {
        return res
    }).catch(res => {
        console.log(res)
        return res
    })
}

// 删除人员信息
export const del_user_info = function(id){
    return axios.post('http://47.108.235.245:8080/api/del_user_info',{
        id,
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 编辑人员信息
export const edit_userlist_info = function(row){
    return axios.post('http://47.108.235.245:8080/api/edit_user_info',{
        id : row.id,
        username : row.username,
        password : row.password,
        root : row.root,
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 添加人员信息
export const add_user_info = function(form){
    return axios.post('http://47.108.235.245:8080/api/add_user_info',{
        name:form.name,
        password:form.password,
        root:form.root
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 删除电表信息
export const delete_info = function(id){
    return axios.post('http://47.108.235.245:8080/api/del_info',{
        id,
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 添加电表 信息
export const add_info = function(form){
    return axios.post('http://47.108.235.245:8080/api/add_info',{
        id:form.id,
        start_numbering:form.start_numbering,
        stop_numbering : form.stop_numbering,
        model : form.model,
        factory : form.factory,
        date : form.date,
        years : form.years,
        cycle : form.cycle,
        appraiser : form.appraiser,
        appraisal_date : form.appraisal_date,
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 编辑电表信息
export const edit_info = function(form){
    return axios.post('http://47.108.235.245:8080/api/edit_info',{
        id : form.id,
        start_numbering : form.start_numbering,
        stop_numbering : form.stop_numbering,
        model : form.model,
        factory : form.factory,
        date : form.date,
        years : form.years,
        cycle : form.cycle,
        appraiser : form.appraiser,
        appraisal_date : form.appraisal_date,
    })
    .then(res => {
        return res
    }).catch(res => {
        return res
    })
}

// 出库列表信息
export const inventory_info = function(){
    return axios.get('http://47.108.235.245:8080/api/inventory')
    .then(res =>{
        return res
    }).catch(res =>{
        console.log(res)
        return res
    })
}
