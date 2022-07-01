
import ajax from './ajax'

/**
 * 系统模块的接口
 */
const system = {
    sliderList(){
        return ajax.get('/system/slider/list/')
    },
}



export {
    system
}
