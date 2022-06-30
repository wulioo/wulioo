//
//
// /** ** 时间搓转换成日期 */
// export function timestampToTime(timestamp) {
//   let date = new Date(timestamp * 1000); // If the time slice is 10 bits, you need to multiply by 1000. If the time slice is 13 bits, you do not need to multiply by 1000
//   let  Y = date.getFullYear() + '-';
//   let  M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1) : date.getMonth()+1) + '-';
//   let  D = date.getDate() + ' ';
//   let  h = date.getHours() + ':';
//   let  m = (date.getMinutes () < 10 ? '0'+(date.getMinutes()) : date.getMinutes ()) + ':';
//   let  s = (date.getSeconds() < 10 ? '0'+(date.getSeconds()) : date.getSeconds ());
//     return Y+M+D+h+m+s;
// }
//
// /**
//  * 获取版本信息
//  * @returns {string}
//  */
// function getDeviceInfo(){
//   let uuid = guid();
//   return JSON.stringify({'reg_keychain': uuid,'devid':uuid,'app_devosver':'web','app_devmodel': 'web'})
// }
//
// /**
//  * 收取版本信息
//  * @returns {string}
//  */
// function getVersionInfo(){
//   return JSON.stringify({"code": 100,"version_code":100,"version_name":"1.0.0"});
// }
//
// /**
//  * 通过localStorage来存储设备信息并且获取
//  * @returns {string[]}
//  */
// export function getDeviceVersion(){
//   let device,version
//   if (localStorage.getItem("deviceInfo") && localStorage.getItem("versionInfo")){
//     device = localStorage.getItem("deviceInfo");
//     version = localStorage.getItem("versionInfo");
//   }else{
//     device = getDeviceInfo();
//     version = getVersionInfo();
//     localStorage.setItem("deviceInfo", device);
//     localStorage.setItem("versionInfo", version);
//   }
//   return {'device':device,'version':version}
// }
//
//
// /**
//  * 生成uuid
//  * @returns {string}
//  */
// function guid() {
//   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
//     var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);
//     return v.toString(16).toUpperCase( );
//   });
// }
//
// export  function browserRedirect() {
//   var sUserAgent = navigator.userAgent.toLowerCase();
//   var bIsIpad = sUserAgent.match(/ipad/i) == "ipad";
//   var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";
//   var bIsMidp = sUserAgent.match(/midp/i) == "midp";
//   var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";
//   var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";
//   var bIsAndroid = sUserAgent.match(/android/i) == "android";
//   var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";
//   var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";
//
//   let bIsMac = sUserAgent.match(/mac/i) == "mac";
//   if(bIsMac){
//     if(window.innerWidth<=1024){
//       bIsIpad = true
//     }
//   }
//
//   if (bIsIpad || bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM) {
//     console.log('iphone start')
//     //跳转移动端页面
//     return
//   }else {
//     window.location.href = process.env.VUE_APP_SKIP_URL
//   }
// }
//
//
//
// /**
//  * 检测是否是Iphone手机
//  * @returns {boolean}
//  */
// export function isPhoneOs($this){
//   let UserAgent = navigator.userAgent.toLowerCase();
//   let IsPhone = UserAgent.match(/iphone os/i) == 'iphone os';
//   let IsPad = UserAgent.match(/ipad/i) == 'ipad'
//   let IsMac = UserAgent.match(/mac/i) == 'mac'
//   if(IsPhone || IsPad ||IsMac ){
//     window.location.href = "https://distribute.kool5.com/index.php?s=/wap/login/index/&t=1&force=1"
//   }else {
//     $this.$alert('请用苹果手机点击下载', '', {
//       type:'warning',
//       customClass:'message-width',
//       showConfirmButton:false,
//       closeOnPressEscape:true,
//     });
//   }
// }
