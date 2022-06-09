import * as S from './Style'
import React, { useEffect } from 'react'

let timeout: ReturnType<typeof setTimeout> | null

const MainTitle = () => {
  useEffect(() => {
    if (!timeout) {
      if (timeout) {
        clearTimeout(timeout)
        timeout = null
      }
    }
  }, [])

  return <S.Container>Hello</S.Container>
}

export default MainTitle
