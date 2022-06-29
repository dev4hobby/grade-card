import React from 'react'
import { useRouter } from 'next/router'
import { dehydrate, QueryClient, useQuery } from 'react-query'
import { fetchUsers } from '../hooks/api/useUsers'
import Link from 'next/link'
import { IUser } from 'src/types/Users'

function Ssr() {
  const { isLoading, error, data } = useQuery<IUser[], Error>('users', () => fetchUsers(10))
  const router = useRouter()
  const { id } = router.query
  const idx = Number(id) - 1

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error...</div>
  return (
    <div className="Detail">
      <Link href="/">
        <a>Go to Index</a>
      </Link>
      {data && (
        <>
          <h1>{data[idx].name}</h1>
          <p>{data[idx].alias}</p>
          <p>{data[idx].id}</p>
        </>
      )}
    </div>
  )
}

export async function getServerSideProps() {
  const queryClient = new QueryClient()

  await queryClient.prefetchQuery('users', () => fetchUsers(10))

  return {
    props: {
      dehydratedState: dehydrate(queryClient),
    },
  }
}

export default Ssr
