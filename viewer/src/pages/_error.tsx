import React from 'react'
import { useRouter } from 'next/router'
import styled from 'styled-components'

function Error({ statusCode, err }: { statusCode: number; err: any }) {
  const router = useRouter()

  console.log(err)

  const handleOnRouteHome = (statusCode: number) => {
    statusCode === 404 ? router.push('/') : router.reload()
  }

  const errorMessage = statusCode === 404 ? '접근할 수 없는 페이지입니다.' : '아래 버튼을 눌러 재시도 해주세요.'

  const buttonLabel = statusCode === 404 ? '홈으로 이동' : '재시도'

  return (
    <PageWrapper>
      <h1>{errorMessage}</h1>
      <ReloadButton onClick={() => handleOnRouteHome(statusCode)}>{buttonLabel}</ReloadButton>
    </PageWrapper>
  )
}

Error.getInitialProps = ({ res, err }: any) => {
  const statusCode = res ? res.statusCode : err ? err.statusCode : 404
  return { statusCode, err }
}

export default Error

export const PageWrapper = styled.div`
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
`

export const ReloadButton = styled.button`
  border-radius: 8px;
  border: 1px solid;
`
