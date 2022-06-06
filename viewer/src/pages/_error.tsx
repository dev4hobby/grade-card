import React from 'react'
import { useRouter } from 'next/router'
import Image from 'next/image'
import colors from '@constants/colors'
import styled from 'styled-components'
import fonts from '@constants/fonts'

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
      <Image src="/assets/emoji_cry.png" alt="bad" width={80} height={80} loading="eager" />
      <Label margin={'20px 0 0 0'}>이용 중 불편을 드려 대단히 죄송합니다.</Label>
      <Label>{errorMessage}</Label>
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

export const Label = styled(fonts.Bold[18])<{ margin?: string }>`
  color: ${colors.GRAY_BASIC_800};
  margin: ${(props) => props.margin && props.margin};
`

export const ReloadButton = styled.button`
  width: 154px;
  height: 40px;
  margin: 20px;
  border-radius: 8px;
  background-color: ${colors.RED_PRIMARY_1_400};
  color: ${colors.GRAY_BASIC_0};
  border: 1px solid ${colors.RED_PRIMARY_1_400};
`
