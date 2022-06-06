import Link from 'next/link'
import React from 'react'
import { dehydrate, QueryClient, useQuery } from 'react-query'
import { fetchUsers } from '../hooks/api/useUsers'
import { IUser } from 'src/types/Users'

const Home = () => {
  const { isLoading, error, data } = useQuery<IUser[], Error>('users', () => fetchUsers(10))

  if (isLoading) return <div>Loading</div>
  if (error) return <div>Error</div>
  return (
    <>
      {data?.map((user: IUser) => (
        <li key={user.id}>
          <div>
            <span>{user.id}. </span>
            <span key={user.id}>
              <Link href={`/ssr/${user.id}`}>{user.alias}</Link>
            </span>
            <a href="#">{user.name}</a>
          </div>
        </li>
      ))}
    </>
  )
}

export async function getStaticProps() {
  const queryClient = new QueryClient()
  await queryClient.prefetchQuery('users', () => fetchUsers(10))

  return {
    props: {
      dehydratedState: dehydrate(queryClient),
    },
  }
}

export default Home
