import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../components/index.vue'),
    children:[
          {
            path: '/',
            name: '人员管理',
            component: () => import('../views/user_list.vue')
          },
          {
              path: '/electric_meter',
              name: '电表信息',
              component: () => import('../views/electric_meter.vue')
          },
          {
            path: '/warehousing',
            name: '电表入库',
            component: () => import('../views/warehousing.vue')
          },
          {
            path: '/inventory',
            name: '设备出库',
            component: () => import('../views/inventory.vue')
          },
          {
            path: '/H',
            name: 'Home',
            component: () => import('../views/Home.vue')
          },
    ]
  },
  {
    path: '/login',
    name: '登录',
    component: () => import('../views/login.vue')
  },
  {
    path: '*',
    name: '404',
    component: () => import('../components/HelloWorld.vue')
  },

]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to , from , next) => {
	console.log(sessionStorage.getItem("value"))

	document.title = '三立-' + to.name
	let token = sessionStorage.getItem("value")
	if(token){
		next()
	}else{
		if(to.path !== '/login'){
			next('/login')
		}else{
			next()
		}
	}

	
})

export default router
