
import {ajax} from './ajax'
import Vue from 'vue'

/**
 * 系统模块的接口
 */
const system = {
    sliderList(){
        return ajax.get('system/slider/list')
    },

}

const sight = {
    sightList(param){
        return ajax.get('sight/sight/list',{params:param})
    },
    sightDetail(pk){
        return ajax.get('sight/sight/detail/' + pk)
    },
    ticketDetail(param){
        return ajax.get('sight/sight/ticket' ,{params:param})
    },
    commentDetail(param){
        return ajax.get('sight/sight/comment' ,{params:param})
    }
}



export {
    system,
    sight
}
