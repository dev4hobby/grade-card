import _ from 'lodash'

export enum test {
  ID = 'ID',
  Name = 'name',
  Questions = 'questions',
}

export interface ITest {
  id: number
  name: string
  questions: JSON
}
