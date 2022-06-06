import _ from 'lodash'

export enum school {
  ID = 'ID',
  Name = 'name',
  Desc = 'desc',
}

export interface ISchool {
  id: number
  name: string
  desc: string
}
