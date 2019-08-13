from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # 解決or非解決
    # サンプル項目4 選択肢
    choice = (
        ("解決", '解決'),
        ("非解決", '非解決'),
    )

    solve = models.CharField(
        verbose_name='選択肢',
        max_length=5,
        choices=choice,
        blank=True,
        null=True,
    )

    # 言語名
    language = models.CharField(
        verbose_name='言語名',
        max_length=20,
        blank=True,
        null=True,
    )

    # タグ or ライブラリ
    tags = models.CharField(
        verbose_name='タグorライブラリ',
        max_length=40,
        blank=True,
        null=True,
    )

    # 内容
    contents = models.TextField(
        verbose_name='内容',
        blank=True,
        null=True,
    )

    # 追記
    add_contents = models.TextField(
        verbose_name='追記',
        blank=True,
        null=True,
    )

    # 日付
    date = models.DateField(
        verbose_name='日付',
        blank=True,
        null=True,
    )

    # 日時
    datetime = models.DateTimeField(
        verbose_name='日時',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.sample_1

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
