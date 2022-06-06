import axios from 'axios'
import { useQuery } from 'react-query'
import { IUser } from 'src/types/Users'

const fetchUsers = async (limit = 10) => {
  const { data } = await axios('localhost:8888/users')
  const result = data.filter((x: IUser) => x.id < limit)
  return result
}

const useUsers = (limit: number) => {
  return useQuery(['users', limit], () => fetchUsers(limit))
}

export { useUsers, fetchUsers }
