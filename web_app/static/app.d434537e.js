(function(e){function t(t){for(var a,i,s=t[0],c=t[1],l=t[2],d=0,p=[];d<s.length;d++)i=s[d],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&p.push(n[i][0]),n[i]=0;for(a in c)Object.prototype.hasOwnProperty.call(c,a)&&(e[a]=c[a]);u&&u(t);while(p.length)p.shift()();return o.push.apply(o,l||[]),r()}function r(){for(var e,t=0;t<o.length;t++){for(var r=o[t],a=!0,s=1;s<r.length;s++){var c=r[s];0!==n[c]&&(a=!1)}a&&(o.splice(t--,1),e=i(i.s=r[0]))}return e}var a={},n={app:0},o=[];function i(t){if(a[t])return a[t].exports;var r=a[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.m=e,i.c=a,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var a in e)i.d(r,a,function(t){return e[t]}.bind(null,a));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/";var s=window["webpackJsonp"]=window["webpackJsonp"]||[],c=s.push.bind(s);s.push=t,s=s.slice();for(var l=0;l<s.length;l++)t(s[l]);var u=c;o.push([0,"chunk-vendors"]),r()})({0:function(e,t,r){e.exports=r("56d7")},"56d7":function(e,t,r){"use strict";r.r(t);r("e260"),r("e6cf"),r("cca6"),r("a79d");var a=r("2b0e"),n=(r("d3b7"),r("bc3a")),o=r.n(n),i={},s=o.a.create(i);s.interceptors.request.use((function(e){return e}),(function(e){return Promise.reject(e)})),s.interceptors.response.use((function(e){return e}),(function(e){return Promise.reject(e)})),Plugin.install=function(e,t){e.axios=s,window.axios=s,Object.defineProperties(e.prototype,{axios:{get:function(){return s}},$axios:{get:function(){return s}}})},a["a"].use(Plugin);Plugin;var c=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("v-app",[a("v-app-bar",{attrs:{app:"",color:"primary",dark:""}},[a("div",{staticClass:"d-flex align-center"},[a("v-img",{staticClass:"shrink mr-2",attrs:{alt:"Vuetify Logo",contain:"",src:r("e958"),transition:"scale-transition",width:"40"}})],1),a("v-spacer"),a("v-btn",{attrs:{href:"https://github.com/vuetifyjs/vuetify/releases/latest",target:"_blank",text:""}})],1),a("v-main",[a("Login",{on:{notify:function(t){return e.notify(t)}}}),a("Notification",{ref:"notification"})],1)],1)},l=[],u=(r("ac1f"),r("1276"),function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-app",{attrs:{id:"inspire"}},[r("v-main",[r("v-container",{staticClass:"fill-height",attrs:{fluid:""}},[r("v-row",{attrs:{align:"center",justify:"center"}},[r("v-col",{attrs:{cols:"12",sm:"8",md:"4"}},[r("v-card",{staticClass:"elevation-12"},[r("v-toolbar",{attrs:{color:"primary",dark:"",flat:""}},[r("v-toolbar-title",[e._v("Canvas-Bot Login")]),r("v-spacer"),r("v-tooltip",{attrs:{bottom:""}})],1),r("v-card-text",[r("v-form",[r("v-text-field",{attrs:{label:"Login",name:"login","prepend-icon":"mdi-account",type:"text"},model:{value:e.username,callback:function(t){e.username=t},expression:"username"}}),r("v-text-field",{attrs:{id:"password",label:"Password",name:"password","prepend-icon":"mdi-lock",type:"password"},model:{value:e.password,callback:function(t){e.password=t},expression:"password"}})],1)],1),r("v-card-actions",[r("v-spacer"),r("Preferences",{attrs:{username:e.username,password:e.password},on:{notify:function(t){return e.$emit("notify",t)}}}),r("register",{on:{notify:function(t){return e.$emit("notify",t)}}})],1)],1)],1)],1)],1)],1)],1)}),d=[],p=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-row",{attrs:{justify:"center"}},[r("v-dialog",{attrs:{persistent:"","max-width":"600px"},scopedSlots:e._u([{key:"activator",fn:function(t){var a=t.on,n=t.attrs;return[r("v-btn",e._g(e._b({attrs:{color:"primary",dark:""}},"v-btn",n,!1),a),[e._v(" Register ")])]}}]),model:{value:e.registration_dialog,callback:function(t){e.registration_dialog=t},expression:"registration_dialog"}},[r("v-card",[r("v-card-title",[r("span",{staticClass:"headline"},[e._v("User Profile")])]),r("v-card-text",[r("v-container",[r("v-row",[r("v-col",{attrs:{cols:"12"}},[r("v-text-field",{attrs:{label:"Username*","prepend-icon":"mdi-account",id:"username",required:""}})],1),r("v-col",{attrs:{cols:"12"}},[r("v-text-field",{attrs:{label:"Email*","prepend-icon":"mdi-at",id:"email",required:""}})],1),r("v-col",{attrs:{cols:"12"}},[r("v-text-field",{attrs:{label:"Password*",type:"password","prepend-icon":"mdi-lock",id:"password",required:""}})],1),r("v-col",{attrs:{cols:"12"}},[r("v-text-field",{attrs:{label:"Confirm Password*",type:"password","prepend-icon":"mdi-lock",id:"confirm_password",required:""}})],1),r("v-col",{attrs:{cols:"12"}},[r("v-text-field",{attrs:{label:"Canvas API Key*",hint:"Find this in your Canvas profile! This is what lets us gather your assignment due dates.","prepend-icon":"mdi-key-variant",id:"api",required:""}})],1)],1)],1),r("small",[e._v("*indicates required field")])],1),r("v-card-actions",[r("v-spacer"),r("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:function(t){e.registration_dialog=!1}}},[e._v("Back")]),r("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:e.post}},[e._v("Submit")])],1)],1)],1),r("v-dialog",{attrs:{persistent:"","max-width":"400px"},model:{value:e.loading_dialog,callback:function(t){e.loading_dialog=t},expression:"loading_dialog"}},[r("v-container",{staticStyle:{height:"200px","background-color":"whitesmoke"}},[r("v-row",{staticClass:"fill-height",attrs:{"align-content":"center",justify:"center"}},[r("v-col",{staticClass:"subtitle-1 text-center",attrs:{cols:"12"}},[e._v(" Creating your account, please wait ")]),r("v-col",{attrs:{cols:"6"}},[r("v-progress-linear",{attrs:{striped:"",color:"primary",indeterminate:"",rounded:"",height:"20"}})],1)],1)],1)],1)],1)},f=[],v=(r("96cf"),r("1da1")),m={data:function(){return{registration_dialog:!1,loading_dialog:!1}},methods:{sleep:function(e){return new Promise((function(t){return setTimeout(t,e)}))},verify_input:function(){var e=!0,t=document.getElementById("username").value,r=document.getElementById("email").value,a=document.getElementById("password").value,n=document.getElementById("confirm_password").value;return""==t||""==a?(e=!1,this.$emit("notify","Username and password cannot be blank!,error")):/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(r)?a!=n&&(e=!1,this.$emit("notify","Passwords do not match!,error")):(e=!1,this.$emit("notify","Invalid email!,error")),e},post:function(){var e=this;this.verify_input()&&(this.loading_dialog=!0,console.log("sending post request"),o.a.post("http://jsonplaceholder.typicode.com/posts",{username:document.getElementById("username").value,email:document.getElementById("email").value,password:document.getElementById("password").value,api:document.getElementById("api").value},{timeout:15e3}).then(function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(r){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.sleep(1e3);case 2:e.loading_dialog=!1,console.log(r),e.registration_dialog=!1,e.$emit("notify","Registration successful!,success");case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()).catch((function(t){e.errors.push(t),e.loading_dialog=!1,e.$emit("notify","Registration failed, please try again!,error")})))}}},g=m,h=r("2877"),b=r("6544"),y=r.n(b),w=r("8336"),_=r("b0af"),x=r("99d9"),k=r("62ad"),V=r("a523"),D=r("169a"),C=r("8e36"),j=r("0fd9"),B=r("2fa4"),P=r("8654"),O=Object(h["a"])(g,p,f,!1,null,null,null),E=O.exports;y()(O,{VBtn:w["a"],VCard:_["a"],VCardActions:x["a"],VCardText:x["b"],VCardTitle:x["c"],VCol:k["a"],VContainer:V["a"],VDialog:D["a"],VProgressLinear:C["a"],VRow:j["a"],VSpacer:B["a"],VTextField:P["a"]});var T=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-row",{attrs:{justify:"center"}},[r("v-dialog",{attrs:{persistent:"","max-width":"400px"},model:{value:e.loading_dialog,callback:function(t){e.loading_dialog=t},expression:"loading_dialog"}},[r("v-container",{staticStyle:{height:"200px","background-color":"whitesmoke"}},[r("v-row",{staticClass:"fill-height",attrs:{"align-content":"center",justify:"center"}},[r("v-col",{staticClass:"subtitle-1 text-center",attrs:{cols:"12"}},[e._v(" Logging you in, please wait ")]),r("v-col",{attrs:{cols:"6"}},[r("v-progress-linear",{attrs:{striped:"",color:"primary",indeterminate:"",rounded:"",height:"20"}})],1)],1)],1)],1),r("v-dialog",{attrs:{persistent:"","max-width":"600px"},scopedSlots:e._u([{key:"activator",fn:function(t){return[r("v-btn",{attrs:{color:"primary",dark:""},on:{click:e.post}},[e._v(" Login ")])]}}]),model:{value:e.preferences_dialog,callback:function(t){e.preferences_dialog=t},expression:"preferences_dialog"}},[r("v-card",[r("v-card-title",[r("span",{staticClass:"headline"},[e._v("User Profile")])]),r("v-card-text",[r("v-container",[r("v-row",[r("v-col",{attrs:{cols:"12",sm:"6"}},[r("v-select",{attrs:{items:["One week before Due Date","Five Days Before Due Date","Three Days Before Due Date","Two Days Before Due Date","One Day Before Due Date","12 Hours Before Due Date","6 Hours Before Due Date","3 Hours Before Due Date","1 Hour Before Due Date","Unsubscribe"],label:"When To Receive Notifications?","item-value":"string",required:""},on:{change:e.map_preferences}})],1)],1)],1),r("small",[e._v("*indicates required field")])],1),r("v-card-actions",[r("v-spacer"),r("v-btn",{attrs:{color:"blue darken-1",text:""},on:{click:e.post}},[e._v("Update Preferences")])],1)],1)],1)],1)},$=[],S={data:function(){return{loading_dialog:!1,preferences_dialog:!1,errors:[],preference:-1}},props:{username:String,password:String},methods:{sleep:function(e){return new Promise((function(t){return setTimeout(t,e)}))},map_preferences:function(e){console.log("PREFERENCE: "+e);var t=-1;switch(e){case"One week before Due Date":t=604800;break;case"Five Days Before Due Date":t=432e3;break;case"Three Days Before Due Date":t=259200;break;case"Two Days Before Due Date":t=172800;break;case"One Day Before Due Date":t=86400;break;case"12 Hours Before Due Date":t=43200;break;case"6 Hours Before Due Date":t=21600;break;case"3 Hours Before Due Date":t=10800;break;case"1 Hours Before Due Date":t=3600;break}console.log("PREFERENCE: "+t),this.preference=t},post:function(){var e=this;this.loading_dialog=!0,console.log("sending post request"),this.preferences_dialog?o.a.post("http://jsonplaceholder.typicode.com/posts",{username:"username",password:"password",preferences:this.preference},{timeout:15e3}).then(function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(r){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.sleep(1e3);case 2:e.loading_dialog=!1,console.log(r),e.preferences_dialog=!1,e.$emit("notify","Preferences updated!,success");case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()).catch((function(t){e.errors.push(t),e.loading_dialog=!1,e.$emit("notify","An unknown error occurred!,error")})):o.a.post("http://jsonplaceholder.typicode.com/posts",{username:"username",password:"password"},{timeout:15e3}).then(function(){var t=Object(v["a"])(regeneratorRuntime.mark((function t(r){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,e.sleep(1e3);case 2:e.loading_dialog=!1,console.log(r),e.preferences_dialog=!0,e.$emit("notify","Login successful!,success");case 6:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}()).catch((function(t){e.errors.push(t),e.loading_dialog=!1,e.$emit("notify","Login failed!,error")}))}}},R=S,L=r("b974"),q=Object(h["a"])(R,T,$,!1,null,null,null),I=q.exports;y()(q,{VBtn:w["a"],VCard:_["a"],VCardActions:x["a"],VCardText:x["b"],VCardTitle:x["c"],VCol:k["a"],VContainer:V["a"],VDialog:D["a"],VProgressLinear:C["a"],VRow:j["a"],VSelect:L["a"],VSpacer:B["a"]});var A={data:function(){return{username:"",password:""}},components:{Preferences:I,Register:E},props:{source:String}},H=A,F=r("7496"),M=r("4bd4"),U=r("f6c4"),N=r("71d9"),J=r("2a7f"),K=r("3a2f"),W=Object(h["a"])(H,u,d,!1,null,null,null),z=W.exports;y()(W,{VApp:F["a"],VCard:_["a"],VCardActions:x["a"],VCardText:x["b"],VCol:k["a"],VContainer:V["a"],VForm:M["a"],VMain:U["a"],VRow:j["a"],VSpacer:B["a"],VTextField:P["a"],VToolbar:N["a"],VToolbarTitle:J["a"],VTooltip:K["a"]});var G=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"text-center ma-2"},[r("v-snackbar",{attrs:{color:e.color,timeout:"2500"},model:{value:e.notify,callback:function(t){e.notify=t},expression:"notify"}},[e._v(" "+e._s(e.text)+" ")])],1)},Q=[],X={data:function(){return{notify:!1,text:"",color:""}},methods:{show_notification:function(e,t){this.text=e,this.color=t,this.notify=!0}}},Y=X,Z=r("2db4"),ee=Object(h["a"])(Y,G,Q,!1,null,"38d55563",null),te=ee.exports;y()(ee,{VSnackbar:Z["a"]});var re={name:"App",components:{Notification:te,Login:z},data:function(){return{}},methods:{notify:function(e){var t=e.split(",");this.$refs.notification.show_notification(t[0],t[1])}}},ae=re,ne=r("40dc"),oe=r("adda"),ie=Object(h["a"])(ae,c,l,!1,null,null,null),se=ie.exports;y()(ie,{VApp:F["a"],VAppBar:ne["a"],VBtn:w["a"],VImg:oe["a"],VMain:U["a"],VSpacer:B["a"]});var ce=r("8c4f"),le=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-app",{attrs:{id:"inspire"}})},ue=[],de={props:{source:String}},pe=de,fe=Object(h["a"])(pe,le,ue,!1,null,null,null),ve=fe.exports;y()(fe,{VApp:F["a"]}),a["a"].use(ce["a"]);var me=[{path:"/",name:"Home",component:ve}],ge=new ce["a"]({routes:me}),he=ge,be=r("f309");a["a"].use(be["a"]);var ye=new be["a"]({});a["a"].config.productionTip=!1,new a["a"]({router:he,vuetify:ye,render:function(e){return e(se)}}).$mount("#app")},e958:function(e,t,r){e.exports=r.p+"img/Canvas-Logo.7389606b.png"}});
//# sourceMappingURL=app.d434537e.js.map