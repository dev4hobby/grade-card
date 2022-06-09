import _ from 'lodash'

export enum question {
  ID = 'ID',
  TypeA = 'typeA', // 연산수행력
  TypeB = 'typeB', // 고차방정식
  Level = 'level', // 난이도
  Answer = 'answer', // 정답 (4)
}

export interface IQuestion {
  id: number
  typeA: string
  typeB: string
  level: string
  answer: string
}
