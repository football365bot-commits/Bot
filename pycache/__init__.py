from sub.done import router as sub_done_router


router = Router(name=__name__)
router.message.filter(IsSubscribedMessage())
router.callback_query.filter(IsSubscribedQuery())


router.include_routers(sub_done_touter,
