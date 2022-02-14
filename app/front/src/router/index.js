import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home'
import Edit from '@/views/Edit'
import NotFound from '@/views/NotFound'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/edit',
    name: 'Create',
    component: Edit
  },
  {
    path: '/edit/:id',
    name: 'EditDetails',
    component: Edit
  },
  {
    path: '/:pathMatch(.*)*',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
