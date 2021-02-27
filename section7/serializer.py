from marshmallow import Schema, fields

class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()
    description = fields.Str()


class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description


# serialize
book = Book("title", "author", "description")

book_schema = BookSchema()
book_dict = book_schema.dump(book)

print(book_dict)
# {"author": "author", "title": "title"}
# description is not existed, because BookSchema does not define description.

# deserialize
# ----------------------------------

incoming_book_data = {
    "title": "title1",
    "author": "author1",
    "description": "description1"
}

book = book_schema.load(incoming_book_data)
print(book)
# raise error, marshmallow found unknown field, description
# and add description field BookSchema and add required option
# { "title": "title1", "author": "author1", "description": "description1" }


# content/models
- 공유 사항을 관리하는 중간테이블("content_sharing_data") 추가

## etc
- get_content_detail_with_permission_check에서 visible을 확인하지 않아서 filter 조건 추가

# contetn/schemas
- 단일항목/전체 목록 조회시 공유 받은 사람을 함께 가져오기 위해 shared_users를 추가

## etc
- 기본정보에 대한 Schema를 추가(UserBasicSchema)

# content/views
- 공유 항목과 공유 대상을 지정하는 contents/sharing_data api 추가
    - 현재까지 약속된 사항으로는 단일 항목을 선택했을 때에만 공유가 가능한 시나리오임, 하지만 현재 작성된 api는 여러 항목을 선택했을 때에도 공유가 가능한 코드 구조임
- 특정 콘텐츠의 공유 대상을 가져오는 contents/<content_id>/shared_users api 추가

## etc
- req.body에 공유사항을 지정하는 공통 Schema를 생성(SharingDataSchema)
- item_ids, user_ids에 0이 들어오면 안되므로 validate 추가 및 error_schemas 추가
- UserBasicSchema를 사용한 ManyUserBasicSchema 추가

# test code
- 성공하는 경우에만 테스트 코드 작성 완료
- 단일항목/전체 목록 조회시 shared_users라는 key가 존재하는지 assert 추가

## etc
- test_api_contents_delete의 success에서 삭제된 항목을 조회하는 api를 진행하면 404 not found가 발생하는데 status_code를 200으로 assert 하고 있음 -> 404로 수정
